test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute(query_q3).fetchall() ==  [('BERNIE 2016', 3),('CARSON AMERICA', 958),('CARLY FOR PRESIDENT', 1000),('CHRIS CHRISTIE FOR PRESIDENT INC', 1000),('CRUZ FOR PRESIDENT', 2000),("O'MALLEY FOR PRESIDENT", 2000),('MARCO RUBIO FOR PRESIDENT', 2460),('KASICH FOR AMERICA INC', 3000),('RAND PAUL FOR US SENATE ', 15000),('DONALD J. TRUMP FOR PRESIDENT, INC.', 19000),('MARCO RUBIO FOR SENATE 2016', 31100),('HILLARY FOR AMERICA', 61200),('CRUZ INFO PRESIDENT', None),('DONALD AND THE PROHET', None),('FOUNDERS COMMITTEE; THE', None),('FUTURE OF AMERICAN LIVES MATTER', None),('GILMORE FOR AMERICA LLC', None),('ITHACA AND TOMPKINS COUNTY FOR BERNIE SANDERS', None),('LAS CRUCES FOR BERNIE', None),('LORAIN COUNTY FORWARD', None)]
          True                                                                       
                      """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
