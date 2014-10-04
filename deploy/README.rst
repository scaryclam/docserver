Deployment
==========

As this project has been built to avoid too many opinions on
how a docserver instance should be set up, so has the deployment.

The deployment strategy that is currently used will always be kept in
the docserver directory here. This may change along with our own requirements,
so please use with care! We may pull out the rug from time to time.
Alternatively, you can put your own deployment ideals in other subfolders
so that you can keep your own deployments in-line with your own requirements.

Docservers deployment
---------------------

We use salt and fabric to provision and deploy the full site. The deployment
should simply be a case of filling in the appropriate secion in the
fabconfig.py file (and the salt manifest if it's a new environment) and then running:

  fab <env> deploy

