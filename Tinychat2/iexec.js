module.exports = {
  name: 'Tinychat2',
  app: {
    type: 'DOCKER',
    envvars: 'XWDOCKERIMAGE=javiermares/tiny-chat',
  },
  work: {
    cmdline: 'python3.6 one-turn.py --config check_tiny --input_string hello',
  }
};
