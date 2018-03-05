module.exports = {
  name: 'miguel-2',
  app: {
    type: 'DOCKER',
    envvars: 'XWDOCKERIMAGE=javiermares/miguel-2',
  },
  work: {
    cmdline: 'python3 /examples/nlp/dime_algo.py',
  }
};
