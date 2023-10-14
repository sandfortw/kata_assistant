from project.services.codewars_service import CodewarsService
import os
from re import sub


class DefaultWriter:
    def __init__(self, url=''):
        self.url = url

    def write_file(self):
        folder_path = os.path.join(os.path.dirname(os.getcwd()), 'codewars_katas')
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
        file.write(f'{self.__determine_language()["import_statment"]} \n\n')
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
        import_statements = {
            'c': '#include "../KATA_ASSISTANT/project/frameworks/c/cw-2"',
            'c#': 'using KATA_ASSISTANT.project.frameworks.csharp.cw_2;',
            'c++': '#include "../KATA_ASSISTANT/project/frameworks/cpp/cw-2"',
            'clojure': ';require [KATA_ASSISTANT.project.frameworks.clojure.cw-2 :as cw-2]',
            'coffeescript': 'cw_2 = require "../KATA_ASSISTANT/project/frameworks/coffeescript/cw-2.coffee"',
            'coq': 'Require Import KATA_ASSISTANT.project.frameworks.coq.cw_2.',
            'crystal': 'require "../KATA_ASSISTANT/project/frameworks/crystal/cw-2"',
            'dart': 'import "package:KATA_ASSISTANT/project/frameworks/dart/cw_2.dart"',
            'elixir': 'alias KATA_ASSISTANT.project.frameworks.elixir.cw_2, as: cw_2',
            'f#': 'open KATA_ASSISTANT.project.frameworks.fsharp.cw_2',
            'go': 'import "KATA_ASSISTANT/project/frameworks/go/cw-2"',
            'groovy': 'import KATA_ASSISTANT.project.frameworks.groovy.cw_2',
            'haskell': 'import KATA_ASSISTANT.project.frameworks.haskell.cw_2',
            'java': 'import KATA_ASSISTANT.project.frameworks.java.cw_2.*',
            'javascript': 'const cw_2 = require("../KATA_ASSISTANT/project/frameworks/javascript/cw-2.js");',
            'kotlin': 'import KATA_ASSISTANT.project.frameworks.kotlin.cw_2.*',
            'lean': 'import KATA_ASSISTANT.project.frameworks.lean.cw_2',
            'lua': 'require "KATA_ASSISTANT.project.frameworks.lua.cw-2"',
            'nasm': 'include KATA_ASSISTANT.project.frameworks.nasm.cw-2',
            'php': 'include "../KATA_ASSISTANT/project/frameworks/php/cw-2.php"',
            'python': 'from KATA_ASSISTANT.project.frameworks.python3.cw_2 import *',
            'racket': '(require KATA_ASSISTANT.project.frameworks.racket.cw-2)',
            'ruby': 'require_relative "../KATA_ASSISTANT/project/frameworks/ruby/cw-2"',
            'rust': 'extern crate KATA_ASSISTANT.project.frameworks.rust.cw_2;',
            'scala': 'import KATA_ASSISTANT.project.frameworks.scala.cw_2._',
            'shell': 'source KATA_ASSISTANT/project/frameworks/shell/cw-2.sh',
            'sql': 'USE KATA_ASSISTANT.project.frameworks.sql.cw_2;',
            'swift': 'import KATA_ASSISTANT.project.frameworks.swift.cw_2',
            'typescript': 'import * as cw_2 from "../KATA_ASSISTANT/project/frameworks/typescript/cw-2";',
            'agda': 'import KATA_ASSISTANT.project.frameworks.agda.cw-2',
            'bf': 'require "../KATA_ASSISTANT/project/frameworks/bf/cw-2.bf"',
            'cfml': '<cfimport prefix="cw_2" from="../KATA_ASSISTANT/project/frameworks/cfml/cw-2.cfm">',
            'cobol': 'COPY KATA_ASSISTANT.project.frameworks.cobol.cw-2',
            'commonlisp': '(require KATA_ASSISTANT.project.frameworks.commonlisp.cw-2)',
            'd': 'import KATA_ASSISTANT.project.frameworks.d.cw_2;',
            'elm': 'import KATA_ASSISTANT.project.frameworks.elm.cw_2 exposing (..)',
            'erlang': '-import(KATA_ASSISTANT.project.frameworks.erlang.cw_2, [function/arity])',
            'factor': 'USING: KATA_ASSISTANT.project.frameworks.factor.cw-2 ;',
            'forth': 'INCLUDE KATA_ASSISTANT.project.frameworks.forth.cw-2',
            'fortran': 'INCLUDE KATA_ASSISTANT.project.frameworks.fortran.cw-2',
            'haxe': 'import KATA_ASSISTANT.project.frameworks.haxe.cw_2;',
            'idris': 'import KATA_ASSISTANT.project.frameworks.idris.cw_2',
            'julia': 'import KATA_ASSISTANT.project.frameworks.julia.cw_2',
            'lambda calculus': '',
            'nim': 'import KATA_ASSISTANT.project.frameworks.nim.cw_2',
            'objective-c': '#import "KATA_ASSISTANT/project/frameworks/objective-c/cw-2.h"',
            'ocaml': 'open KATA_ASSISTANT.project.frameworks.ocaml.cw_2',
            'pascal': 'uses KATA_ASSISTANT.project.frameworks.pascal.cw-2;',
            'perl': 'use KATA_ASSISTANT.project.frameworks.perl.cw_2;',
            'powershell': 'Import-Module KATA_ASSISTANT.project.frameworks.powershell.cw-2',
            'prolog': 'consult("KATA_ASSISTANT/project/frameworks/prolog/cw-2.pl").',
            'purescript': 'import KATA_ASSISTANT.project.frameworks.purescript.cw_2',
            'r': 'source("KATA_ASSISTANT/project/frameworks/R/cw-2.R")',
            'raku': 'use KATA_ASSISTANT.project.frameworks.raku.cw-2;',
            'reason': 'open KATA_ASSISTANT.project.frameworks.reason.cw_2;',
            'risc-v': 'import KATA_ASSISTANT.project.frameworks.riscv.cw_2',
            'solidity': 'import * as cw_2 from "../KATA_ASSISTANT/project/frameworks/solidity/cw-2";',
            'vb.net': 'Imports KATA_ASSISTANT.project.frameworks.vbnet.cw_2'
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