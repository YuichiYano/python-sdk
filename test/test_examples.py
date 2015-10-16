# coding=utf-8

import os
import watson_developer_cloud
import pytest
import sys
from os import getcwd
from subprocess import Popen, PIPE
from os.path import join, dirname
from glob import glob

# tests to exclude
excludes = ['authorization_v1.py',
            'language_translation_v2.py', 'concept_expansion_v1.py', 'question_and_answer_v1_beta.py']
# examples path. /examples
examples_path = join(dirname(__file__), '../', 'examples', '*.py')

# environment variables
try:
    from dotenv import load_dotenv
    dotenv_path = join(dirname(__file__), '../', '.env')
    load_dotenv(dotenv_path)
except:
    print 'WARNING: dotenv could not be imported'
    pass

@pytest.mark.skipif(os.getenv('VCAP_SERVICES') is None, reason='requires VCAP_SERVICES')
def test_examples():
    examples = glob(examples_path)
    for example in examples:
        name = example.split('/')[-1]
        # exclude some tests cases like authorization
        if name in excludes:
            continue

        p = Popen(['python', example], stdout=PIPE, stderr=PIPE, stdin=PIPE)
        out, err = p.communicate()

        assert p.returncode == 0, 'example %s fail with error: %s' % (
            name, err)
