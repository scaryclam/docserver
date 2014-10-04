import os

# Import default settings for the project

# We use an environmental variable to indicate the, erm, environment
# This block writes all settings to the local namespace
module_path = os.environ.get('DJANGO_CONF', 'conf.local')
try:
    module = __import__(module_path, globals(), locals(), ['*'])
except ImportError, err:
    import sys
    print "You need to create a file {0} to contain your local settings, or fix {1}".format(module_path, err)
    sys.exit(1)

for k in dir(module):
    if not k.startswith("__"):
        locals()[k] = getattr(module, k)

