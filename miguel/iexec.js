module.exports = {
  name: 'Miguel',
  app: {
    type: 'DOCKER',
    envvars: 'XWDOCKERIMAGE=javiermares/miguel',
  },
  work: {
    cmdline: 'python3 /examples/nlp/dime_algo.py',
  }
};
