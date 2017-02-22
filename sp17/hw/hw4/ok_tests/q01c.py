test = {
  'name': 'Question 1c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> connection.execute(query_q1c).fetchall() == [('C00496075', 'RAND PAUL FOR PRESIDENT, INC.', 1400000),('C00492785', 'CRUZ FOR PRESIDENT', 250012),('C00027466', 'MARCO RUBIO FOR US SENATE', 46800),('C00570739', 'CRUZ FOR PRESIDENT', 30619),('C00436410', 'RAND PAUL FOR U.S. SENATE', 20000),('C00193631', 'MARCO RUBIO FOR U.S. SENATE', 17500),('C00409003', 'MARCO RUBIO FOR US SENATE', 15000),('C00051979', 'KASICH FOR AMERICA', 15000),('C00197863', 'HILLARY VICTORY FUND', 15000),('C00283523', 'CRUZ FOR PRESIDENT', 15000),('C00296657', 'KASICH FOR AMERICA', 12400),('C00235572', 'RAND PAUL FOR US SENATE 2016', 10000),('C00457705', 'MARCO RUBIO SENATE 2016', 10000),('C00525600', 'HILLARY FOR AMERICA', 10000),('C00344648', 'MARCO RUBIO FOR SENATE 2016', 10000),('C00507574', 'HILLARY FOR AMERICA', 10000),('C00497842', 'RUBIO VICTORY COMMITTEE', 10000),('C00575340', 'KASICH FOR AMERICA', 10000),('C00089136', 'RAND PAUL FOR US SENATE 2016', 10000),('C00400929', 'MARCO RUBIO FOR SENATE 2016', 10000)]
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
