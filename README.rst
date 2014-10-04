Docserver
========

Docserver is a simple document server, build to auto build documentation,
from source control repositories.

Motivation
----------

This sounds a lot like readthedocs.org, right? Well, yes and no. readthedocs.org is actually
the driving factor behind this project. I needed a service like readthedocs that I could install
on an internal server adn pull from private repositories. readthedocs is very opinionated (the code, not
necessarily the developers!) about the technologies, which made doing this much more effort than simply
creating a document server targeted at internal use rather than a document hosting service.

Readthedocs.org is an excellent site and I strongly advise developers and document writers
to use it over this project if you do not need an internal solution!

Docserver is being built to be a more modular system that will allow developers
to create private code repositories and auhto-build their documentation without
having to change their own internal development practices or install and use
technologies that may go against internal policy.

Deployment
----------

There is an existing deployment setup in the deploy directory. The docserver deployment
is the currently used deployment strategy. This is suited to docservers needs but you
can fork it and use it if you like.

Please refer to the README in the deploy directory for up-to-date deployment instructions.
