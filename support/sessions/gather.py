import json
import os

class Sessions:
    def __init__(self, directory):
        self.directory = directory

    def structure(self):
        return [Session(session) for session in os.listdir(self.directory) if os.path.isdir(os.path.join(self.directory, session)) and session.startswith('session')]

class Session:
    def parse(input):
        url = os.path.join(input, "index.html")
        parts = input.split('-')
        name = parts[0].capitalize() + ' ' + str(int(parts[1]) + 1)
        return {'name': name, 'url': url}

    def __init__(self, input):
        structure = Session.parse(input)
        self.name = structure['name']
        self.url = structure['url']
    
    def structure(self):
        return {'name': self.name, 'url': self.url}


class SessionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Session) or isinstance(obj, Sessions):
            return obj.structure()
        else:
            return json.JSONEncoder.default(self, obj) 


if __name__ == '__main__':
    directory = '../../docs/presentation/'
    sessions = Sessions(directory)
    output = json.dumps(sessions, cls=SessionEncoder)

    f = open(os.path.join(directory, 'presentations.json'), 'w')
    f.write(output)
    f.close
    