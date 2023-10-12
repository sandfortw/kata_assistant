from project.services.codewars_service import CodewarsService
import os
from re import sub


class DefaultWriter:
    def __init__(self, url='', location=os.path.expanduser("~/Desktop")):
        self.url = url
        self.location = location

    def write_file(self):
        folder_path = os.path.join(self.location, 'codewars_katas')
        os.makedirs(folder_path, exist_ok=True)
        data = CodewarsService().get_challenge_info(challenge_url = self.url)
        '''
        Test URLs:
        
        Python:
        https://www.codewars.com/kata/520446778469526ec0000001/train/python
         
        Ruby:
        https://www.codewars.com/kata/5518a860a73e708c0a000027/train/ruby
        '''
        code = self.__codify(data['code'])
        snake_cased_challenge_name = self.__snake_case(data['name'])
        file = open(f"{folder_path}/{snake_cased_challenge_name}{self.__determine_language()['extension']}", "w")
        file.write(f'{self.__determine_language()["comment_char"]}CODE: \n')
        file.write(code['challenge_code'] + '\n')
        file.write(f'\n{self.__determine_language()["comment_char"]}TEST:\n')
        file.write(code['test_code'])
        print(f"{snake_cased_challenge_name}{self.__determine_language()['extension']} created at {folder_path}") 

    def __codify(self, code_data):
        return code_data



    def __determine_language(self):
        parts = self.url.split("/")
        language = parts[-1]
        language_file_extensions = {
            'c': '.c',
            'c#': '.cs',
            'c++': '.cpp',
            'clojure': '.clj',
            'coffeescript': '.coffee',
            'coq': '.v',
            'crystal': '.cr',
            'dart': '.dart',
            'elixir': '.ex',
            'f#': '.fs',
            'go': '.go',
            'groovy': '.groovy',
            'haskell': '.hs',
            'java': '.java',
            'javascript': '.js',
            'kotlin': '.kt',
            'lean': '.lean',
            'lua': '.lua',
            'nasm': '.asm',
            'php': '.php',
            'python': '.py',
            'racket': '.rkt',
            'ruby': '.rb',
            'rust': '.rs',
            'scala': '.scala',
            'shell': '.sh',
            'sql': '.sql',
            'swift': '.swift',
            'typescript': '.ts',
            'agda': '.agda',
            'bf': '.bf',
            'cfml': '.cfml',
            'cobol': '.cob',
            'commonlisp': '.lisp',
            'd': '.d',
            'elm': '.elm',
            'erlang': '.erl',
            'factor': '.factor',
            'forth': '.4th',
            'fortran': '.f90',
            'haxe': '.hx',
            'idris': '.idr',
            'julia': '.jl',
            'lambda calculus': '',
            'nim': '.nim',
            'objective-c': '.m',
            'ocaml': '.ml',
            'pascal': '.pas',
            'perl': '.pl',
            'powershell': '.ps1',
            'prolog': '.pl',
            'purescript': '.purs',
            'r': '.r',
            'raku': '.raku',
            'reason': '.re',
            'risc-v': '.riscv',
            'solidity': '.sol',
            'vb.net': '.vb'
        }
        language_comment_characters = {
            'c': '//',
            'c#': '//',
            'c++': '//',
            'clojure': ';;',
            'coffeescript': '#',
            'coq': '(*...*)',
            'crystal': '#',
            'dart': '//',
            'elixir': '#',
            'f#': '//',
            'go': '//',
            'groovy': '//',
            'haskell': '--',
            'java': '//',
            'javascript': '//',
            'kotlin': '//',
            'lean': '--',
            'lua': '--',
            'nasm': ';',
            'php': '//',
            'python': '#',
            'racket': ';;',
            'ruby': '#',
            'rust': '//',
            'scala': '//',
            'shell': '#',
            'sql': '--',
            'swift': '//',
            'typescript': '//',
            'agda': '--',
            'bf': '',  # Brainfuck has no one-line comments
            'cfml': '//',
            'cobol': '*',
            'commonlisp': ';;',
            'd': '//',
            'elm': '--',
            'erlang': '%',
            'factor': '!',
            'forth': '\\',
            'fortran': '!',
            'haxe': '//',
            'idris': '--',
            'julia': '#',
            'lambda calculus': '',  # Lambda Calculus has no comments
            'nim': '#',
            'objective-c': '//',
            'ocaml': '//',
            'pascal': '//',
            'perl': '#',
            'powershell': '#',
            'prolog': '%',
            'purescript': '--',
            'r': '#',
            'raku': '#',
            'reason': '/*...*/',
            'risc-v': '#',
            'solidity': '//',
            'vb.net': "'"
        }

        return {
            'language': language,
            'extension': language_file_extensions[language],
            'comment_char': language_comment_characters[language],
        }
    
    def __snake_case(self, s):
        return '_'.join(
            sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
            s.replace('-', ' '))).split()).lower()