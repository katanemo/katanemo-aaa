import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';
import {readFileSync} from 'fs';
const SCHEMA_FILE='<schema_file_path>'
const typeDefs = readFileSync(SCHEMA_FILE, 'utf-8');

let estates = [
  {
    id: '1',
    displayName: 'Kirkland Beach House',
  },
  {
    id: '2',
    displayName: 'Leverett House',
  },
  {
    id: '3',
    displayName: 'Quincy House',
  },
  {
    id: '4',
    displayName: 'Winthrop Lake House',
  }
]

const resolvers = {
  PureQuery: {
    estate: (parent, args, context, info) => {
      const estate = estates.find(e => e.id === args.id)
      return estate
    },
  },
  PureMutation: {
    createEstate: (parent, args, context, info) => {
      const estate = {
        id: String(estates.length + 1),
        displayName: args.input.attributes["displayName"]
      }
      estates.push(estate)
      return {
        clientMutationId: Math.random().toString(),
        estate: estate
      }
    }
  }
};

const server = new ApolloServer({
  typeDefs,
  resolvers,
  plugins: [
  ]
});

const { url } = await startStandaloneServer(server, {
  listen: { port: 4000 },
});

console.log(`🚀  Server ready at: ${url}`);
