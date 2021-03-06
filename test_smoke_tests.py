#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Crash Tests Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): David Burns
#                 Matt Brandt <mbrandt@mozilla.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

from crash_stats_page import CrashStatsHomePage
from crash_stats_page import CrashStatsSearchResults
from unittestzero import Assert
import pytest
xfail = pytest.mark.xfail

class TestSmokeTests:


    def test_that_server_status_page_loads(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        csstat = csp.click_server_status()
        try:
            csstat.at_a_glance()
        except Exception, e:
            Assert.fail(str(e))

        try:
            csstat.graphs()
        except Exception, e:
            Assert.fail(str(e))

        try:
            csstat.latest_raw_stats()
        except Exception, e:
            Assert.fail(str(e))

    @xfail(reason="Disabled till Bug 612679 is fixed")
    def test_that_options_are_sorted_the_same(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        cssearch = csp.click_advanced_search()
        nav_product_list = csp.product_list
        search_product_list = cssearch.product_list
        Assert.equal(len(nav_product_list),len(search_product_list))
        for i, prod_item in enumerate(nav_product_list):
            Assert.equal(prod_item, search_product_list[i])

    def test_that_advanced_search_has_firefox_highlighted_in_multiselect(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        cs_advanced = csp.click_advanced_search()
        Assert.equal('Firefox', cs_advanced.currently_selected_product)

    def test_that_advanced_search_has_thunderbird_highlighted_in_multiselect(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        csp.select_product('Thunderbird')
        cs_advanced = csp.click_advanced_search()
        Assert.equal('Thunderbird', cs_advanced.currently_selected_product)
    
    def test_that_advanced_search_has_fennec_highlighted_in_multiselect(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        csp.select_product('Fennec')
        cs_advanced = csp.click_advanced_search()
        Assert.equal('Fennec', cs_advanced.currently_selected_product)
    
    def test_that_advanced_search_has_camino_highlighted_in_multiselect(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        csp.select_product('Camino')
        cs_advanced = csp.click_advanced_search()
        Assert.equal('Camino', cs_advanced.currently_selected_product)

    def test_that_advanced_search_has_seamonkey_highlighted_in_multiselect(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        csp.select_product('SeaMonkey')
        cs_advanced = csp.click_advanced_search()
        Assert.equal('SeaMonkey', cs_advanced.currently_selected_product)

    @xfail(reason="Disabled till Bug 652880 is fixed")
    def test_that_advanced_search_view_signature_for_firefox_crash(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        cs_advanced = csp.click_advanced_search()
        cs_advanced.filter_reports()
        if not cs_advanced.can_find_text('no data'):
            signature = cs_advanced.click_first_signature()
            Assert.true(signature in cs_advanced.page_heading)

    def test_that_advanced_search_view_signature_for_thunderbird_crash(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        csp.select_product('Thunderbird')
        cs_advanced = csp.click_advanced_search()
        cs_advanced.filter_reports()
        if not cs_advanced.can_find_text('no data'):
            signature = cs_advanced.click_first_signature()
            Assert.true(signature in cs_advanced.page_heading)

    def test_that_advanced_search_view_signature_for_fennec_crash(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        csp.select_product('Fennec')
        cs_advanced = csp.click_advanced_search()
        cs_advanced.filter_reports()
        if not cs_advanced.can_find_text('no data'):
            signature = cs_advanced.click_first_signature()
            Assert.true(signature in cs_advanced.page_heading)

    def test_that_advanced_search_view_signature_for_camino_crash(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        csp.select_product('Camino')
        cs_advanced = csp.click_advanced_search()
        cs_advanced.filter_reports()
        if not cs_advanced.can_find_text('no data'):
            signature = cs_advanced.click_first_signature()
            Assert.true(signature in cs_advanced.page_heading)

    def test_that_advanced_search_view_signature_for_seamonkey_crash(self, testsetup):
        self.selenium = testsetup.selenium
        csp = CrashStatsHomePage(testsetup)
        csp.select_product('SeaMonkey')
        if not csp.can_find_text('no data'):
            cs_advanced = csp.click_advanced_search()
            cs_advanced.filter_reports()
            if not cs_advanced.can_find_text('No Data'): 
                signature = cs_advanced.click_first_signature()
                Assert.true(signature in cs_advanced.page_heading)

    def test_that_simple_querystring_doesnt_return_500(self, testsetup):
        import urllib
        response = urllib.urlopen( testsetup.base_url + "/query/simple")
        Assert.equal(404, response.getcode())
