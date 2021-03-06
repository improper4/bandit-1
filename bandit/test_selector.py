# -*- coding:utf-8 -*-
#
# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


def checks_functions(func):
    '''
    Use of this delegate before a test function indicates that it should be
    called any time a function call is encountered.
    '''
    if not hasattr(func, "_checks"):
        func._checks = []
    func._checks.append("functions")
    return func


def checks_imports(func):
    '''
    Use of this delegate before a test function indicates that it should be
    called any time an import is encountered.
    '''
    if not hasattr(func, "_checks"):
        func._checks = []
    func._checks.append("imports")
    return func


def checks_strings(func):
    '''
    Use of this delegate before a test function indicates that it should be
    called any time a string value is encountered.
    '''
    if not hasattr(func, "_checks"):
        func._checks = []
    func._checks.append("strings")
    return func


def takes_config(func):
    '''
    Use of this delegate before a test function indicates that it should be
    passed data from the config file
    '''
    if not hasattr(func, "_takes_config"):
        func._takes_config = True
    return func
