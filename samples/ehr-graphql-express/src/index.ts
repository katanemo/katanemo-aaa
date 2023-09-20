import { createServer } from 'node:http'
import { createYoga } from 'graphql-yoga'
import { createTags, getShortTermToken, useKauth } from './kauth/index.js'
import { makeExecutableSchema } from '@graphql-tools/schema';
import dotenv from 'dotenv';
import {  useLogger, useSchema } from '@envelop/core';
import { readFileSync } from 'fs';

dotenv.config();

function makeid(length: number) {
  let result = '';
  const characters = 'abcdefghijklmnopqrstuvwxyz0123456789';
  const charactersLength = characters.length;
  let counter = 0;
  while (counter < length) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
    counter += 1;
  }
  return result;
}

const SCHEMA_FILE = `schema.graphql`

const typeDefs = readFileSync(SCHEMA_FILE, 'utf-8');

const patients = [
  { id: '1', name: 'Matt Damon' },
  { id: '2', name: 'Mike Clarkson' },
  { id: '3', name: 'John Woo' }
]

const katanemoApiAccessToken = await getShortTermToken(process.env.clientId, process.env.clientSecret, process.env.apiEndpoint)

const resolvers = {
  Query: {
    getPatient: (_, { id }) => {
      return patients.find(patient => patient.id === id)
    },
  },
  Mutation: {
    createPatient: async (_: any, { patientInput }: any, context) => {
      const patientId = makeid(8);
      const newPatient = { id: patientId, ...patientInput }
      patients.push(newPatient)
      // add tags for newly created patient
      const resp = await createTags(context, 'patient', patientId, {}, process.env.apiEndpoint)
      if (resp.status !== 200) {
        throw new Error(`Failed to create tags for patient ${patientId}`)
      }
      return newPatient
    }
  }
}

const ehrServiceSchema = makeExecutableSchema({
  typeDefs,
  resolvers
});

const yoga = createYoga({
  plugins: [
    useSchema(ehrServiceSchema),
    useLogger(),
    useKauth({
      serviceId: process.env.serviceId,
      accessToken: katanemoApiAccessToken,
      clientId: process.env.clientId,
      clientSecret: process.env.clientSecret,
    })
  ]
})

const server = createServer(yoga)

server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
