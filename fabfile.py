from fabric.api import local, run, env, lcd, cd, sudo
from fabric.operations import put
from fabric.context_managers import shell_env, prefix
from fabric.decorators import with_settings

env.hosts = ['step.polymtl.ca']
env.user = 'fgiraldeau'

homedir = '/home/etudiant/fgiraldeau/'
basedir = homedir + 'nova_html'

def deploy():
    with cd(basedir):
        run("git pull origin master")

