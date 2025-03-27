
import sys
sys.executable

from Tests.searchCity import SearchCity

'''
Deacription: 	Search City Name for Weather Forecast
'''

setUpClass = SearchCity()
setUpClass.setUpClass()

# test_01_search_valid_city = SearchCity()
# test_01_search_valid_city.test_01_search_valid_city()

test_02_search_invalid_city = SearchCity()
test_02_search_invalid_city.test_02_search_invalid_city()

tearDownClass = SearchCity()
tearDownClass.tearDownClass()