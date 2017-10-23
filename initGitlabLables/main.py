import urllib.request
import urllib.error
import urllib.parse
import urllib.request
import urllib.parse
import urllib.error
import configparser
import argparse


class Label(object):

    def __init__(self, name, color):
        super(Label, self).__init__()
        self.name = name
        self.color = color


class LabelService(object):
    def __init__(self, apiUrl,
                 project,
                 token,
                 ):
        super(LabelService, self).__init__()
        self.apiUrl = apiUrl
        self.token = token
        self.project = project

    def add_label(self, label: Label):
        print("add_label: ", label.name)
        self.postOrDelete(label, 'POST')

    def delete_label(self, label: Label):
        print("delete_label: ", label.name)
        self.postOrDelete(label, 'DELETE')

    def postOrDelete(self, label, method):
        req = urllib.request.Request(
            # http://10.186.18.21/api/v4/projects/86/labels
            self.apiUrl + '/projects/' + self.project + '/labels',
            data=urllib.parse.urlencode(
                {'name': label.name, 'color': label.color}).encode('ascii'))
        print(self.apiUrl + '/projects/' + self.project + '/labels')
        req.add_header('PRIVATE-TOKEN', self.token)
        if method == 'DELETE':
            req.get_method = lambda: 'DELETE'
        elif method == 'POST':
            req.get_method = lambda: 'POST'

        with urllib.request.urlopen(req) as resp:
            resp.read()


def getLabels(config=configparser.ConfigParser):
    labels = []
    for opt in config.options('labels'):
        labels.append(Label(opt, config.get('labels', opt)))
    return labels


config = configparser.ConfigParser()
config.read("./config")
labels = getLabels(config)
svc = LabelService(
    config.get('global', 'api'),
    config.get('global', 'project'),
    config.get('global', 'private-token'),
)
# tryBest = config.getBool('global', 'raise_error')
parser = argparse.ArgumentParser(description='Operator Gitlab labels.')
parser.add_argument('--delete', action='store_true', default=False,
                    help='delete labels listed in config instead of add')
parser.add_argument('--raise_error', action='store_true', default=False,
                    help='program will abend if meet any error')

args = parser.parse_args()
msg = 'add label'
if args.delete:
    msg = 'delete label'
for x in labels:
    try:
        if args.delete:
            svc.delete_label(x)
        else:
            svc.add_label(x)
    except Exception as e:
        if args.raise_error:
            raise e
        print(msg, x.name, 'faild, error: ', e)
