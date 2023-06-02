
# Katanemo Documentation Contribution Guide

To edit pages, please go to it's respective `.md` file in the `/docs` folder. Use GitHub markdown styles to edit the page. You can also directly edit the page within GitHub with the pencil icon or use ann IDE.

## Building

Start by accessing the `/docs` folder:
```
cd docs
```

Then, please install the dependencies:
```
npm install
```

Finally, start the server:
```
npm start
```

To **build** the documentation, and use local search:
```
npm run build && npm run serve
```

The `docusaurus.config.js` file should not be touched. It's the configuration file and everything is already configured. If your using the search function, make sure that the `typesense` search is commented out of this file.

Other questions? Refer to the [Docusaurus documentation.](https://docusaurus.io/docs/)
