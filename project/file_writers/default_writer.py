from project.services.codewars_service import CodewarsService
import os
from re import sub


class DefaultWriter:
    def __init__(self, url=''):
        self.url = url

    def write_file(self):
        folder_path = os.path.join(os.getcwd(), 'codewars_katas')
        os.makedirs(folder_path, exist_ok=True)
        data = CodewarsService().get_challenge_info(challenge_url = self.url)
        '''
        Test URLs:
        
        Python:
        https://www.codewars.com/kata/520446778469526ec0000001/train/python
         
        Ruby:
        https://www.codewars.com/kata/5518a860a73e708c0a000027/train/ruby
        '''
        language_data = self.__determine_language()
        code = self.__codify(data['code'], language_data)
        snake_cased_challenge_name = self.__snake_case(data['name'])
        file = open(f"{folder_path}/{snake_cased_challenge_name}{self.__determine_language()['extension']}", "w")
        file.write(f'{language_data["import_statment"]} \n\n')
        file.write(f'{language_data["comment_char"]}CODE: \n')
        file.write(code['challenge_code'] + '\n')
        file.write(f'\n{language_data["comment_char"]}TEST:\n')
        file.write(code['test_code'])
        print(f"{snake_cased_challenge_name}{language_data['extension']} created at {folder_path}") 

    def __codify(self, code_data, language_data):
        language = language_data['language']
        comment_char = language_data['comment_char']
        match language: 
            case 'python':
                """
                    Comment out the first 2 lines of the test code,
                    which in most cases will allow the tests to run 
                    without futher modification. 
                """
                data_array = code_data['test_code'].split('\n')
                for x in (0,1):
                    data_array[x] = comment_char + data_array[x]
                test_code = "\n".join(data_array)
                code_data['test_code'] = test_code
            case _:
                pass
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

        import_statements = {
            #Functional:
            'javascript': 'require("../project/frameworks/javascript/cw-2.js");',
            'python': 'import codewars_test as test',
            'ruby': 'require_relative "../project/frameworks/ruby/cw-2"',
            #Not yet tested:
            'c': '#include "../project/frameworks/c/cw-2"',
            'c#': 'using project.frameworks.csharp.cw_2;',
            'c++': '#include "../project/frameworks/cpp/cw-2"',
            'clojure': ';require [project.frameworks.clojure.cw-2 :as cw-2]',
            'coffeescript': 'cw_2 = require "../project/frameworks/coffeescript/cw-2.coffee"',
            'coq': 'Require Import project.frameworks.coq.cw-2.',
            'crystal': 'require "../project/frameworks/crystal/cw-2"',
            'dart': 'import "package:project/frameworks/dart/cw_2.dart"',
            'elixir': 'alias project.frameworks.elixir.cw-2, as: cw_2',
            'f#': 'open project.frameworks.fsharp.cw-2',
            'go': 'import "project/frameworks/go/cw-2"',
            'groovy': 'import project.frameworks.groovy.cw-2',
            'haskell': 'import project.frameworks.haskell.cw-2',
            'java': 'import project.frameworks.java.cw-2.*',
            'kotlin': 'import project.frameworks.kotlin.cw-2.*',
            'lean': 'import project.frameworks.lean.cw-2',
            'lua': 'require "project/frameworks/lua/cw-2"',
            'nasm': 'include project.frameworks.nasm.cw-2',
            'php': 'include "../project/frameworks/php/cw-2.php"',
            'racket': '(require project.frameworks.racket.cw-2)',
            'rust': 'extern crate project.frameworks.rust.cw_2;',
            'scala': 'import project.frameworks.scala.cw_2._',
            'shell': 'source project/frameworks/shell/cw-2.sh',
            'sql': 'USE project.frameworks.sql.cw-2;',
            'swift': 'import project.frameworks.swift.cw-2',
            'typescript': 'import * as cw_2 from "../project/frameworks/typescript/cw-2";',
            'agda': 'import project.frameworks.agda.cw-2',
            'bf': 'require "../project/frameworks/bf/cw-2.bf"',
            'cfml': '<cfimport prefix="cw_2" from="../project/frameworks/cfml/cw-2.cfm">',
            'cobol': 'COPY project.frameworks.cobol.cw-2',
            'commonlisp': '(require project.frameworks.commonlisp.cw-2)',
            'd': 'import project.frameworks.d.cw_2;',
            'elm': 'import project.frameworks.elm.cw_2 exposing (..)',
            'erlang': '-import(project.frameworks.erlang.cw_2, [function/arity])',
            'factor': 'USING: project.frameworks.factor.cw-2 ;',
            'forth': 'INCLUDE project.frameworks.forth.cw-2',
            'fortran': 'INCLUDE project.frameworks.fortran.cw-2',
            'haxe': 'import project.frameworks.haxe.cw_2;',
            'idris': 'import project.frameworks.idris.cw_2',
            'julia': 'import project.frameworks.julia.cw_2',
            'lambda calculus': '',
            'nim': 'import project.frameworks.nim.cw-2',
            'objective-c': '#import "project/frameworks/objective-c/cw-2.h"',
            'ocaml': 'open project.frameworks.ocaml.cw-2',
            'pascal': 'uses project.frameworks.pascal.cw-2;',
            'perl': 'use project.frameworks.perl.cw-2;',
            'powershell': 'Import-Module project.frameworks.powershell.cw-2',
            'prolog': 'consult("project/frameworks/prolog/cw-2.pl").',
            'purescript': 'import project.frameworks.purescript.cw-2',
            'r': 'source("project/frameworks/R/cw-2.R")',
            'raku': 'use project.frameworks.raku.cw-2;',
            'reason': 'open project.frameworks.reason.cw-2;',
            'risc-v': 'import project.frameworks.riscv.cw-2',
            'solidity': 'import * as cw_2 from "../project/frameworks/solidity/cw-2";',
            'vb.net': 'Imports project.frameworks.vbnet.cw-2'
        }
        
        return {
            'language': language,
            'extension': language_file_extensions[language],
            'comment_char': language_comment_characters[language],
            'import_statment': import_statements[language]
        }
    
    def __snake_case(self, s):
        return '_'.join(
            sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
            s.replace('-', ' '))).split()).lower()