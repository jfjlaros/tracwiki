"""
tracwiki: Checkout and commit wiki pages stored on a trac server.


First use the config option to configure the server, after this, the checkout
and commit commands are available.

Copyright (c) 2012 Jeroen F.J. Laros <jlaros@fixedpoint.nl>
Licensed under the MIT license, see the LICENSE file.
"""

# On the event of a new release, we update the __version_info__ package
# global and set RELEASE to True.
# Before a release, a development version is denoted by a __version_info__
# ending with a 'dev' item and RELEASE is set to False.
#
# We follow a versioning scheme compatible with setuptools [1] where the
# __version_info__ variable always contains the version of the upcomming
# release (and not that of the previous release), post-fixed with a 'dev'
# item. Only in a release commit, this 'dev' item is removed (and added
# again in the next commit).
#
# [1] http://peak.telecommunity.com/DevCenter/setuptools#specifying-your-project-s-version

RELEASE = False

__version_info__ = ('0', '13', '1')


__version__ = '.'.join(__version_info__)
__author__ = 'Jeroen F.J. Laros'
__contact__ = 'jlaros@fixedpoint.nl'
__homepage__ = 'https://www.fixedpoint.nl'

usage = __doc__.split("\n\n\n")

def docSplit(func):
    return func.__doc__.split("\n\n")[0]

def version(name):
    return "%s version %s\n\nAuthor   : %s <%s>\nHomepage : %s" % (name,
        __version__, __author__, __contact__, __homepage__)
