test = {
  'name': 'Question 1c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> connection.execute(query_q1c).fetchall() == [('C00492785', 'CRUZ FOR PRESIDENT', 250012),('C00570739', 'CRUZ FOR PRESIDENT', 30619),('C00193631', 'MARCO RUBIO FOR U.S. SENATE', 17500),('C00197863', 'HILLARY VICTORY FUND', 15000),('C00283523', 'CRUZ FOR PRESIDENT', 15000),('C00051979', 'KASICH FOR AMERICA', 15000),('C00296657', 'KASICH FOR AMERICA', 12400),('C00431601', 'HILLARY FOR AMERICA', 10000),('C00365270', 'HILLARY FOR AMERICA', 10000),('C00300376', 'HILLARY FOR AMERICA', 10000),('C00400333', 'HILLARY FOR AMERICA', 10000),('C00409003', 'MARCO RUBIO FOR US SENATE', 10000),('C00342048', 'HILLARY FOR AMERICA', 10000),('C00538835', 'HILLARY FOR AMERICA', 10000),('C00399642', 'MARCO RUBIO FOR US SENATE', 10000),('C00497842', 'RUBIO VICTORY COMMITTEE', 10000),('C00193433', 'HILLARY FOR AMERICA', 10000),('C00362384', 'HILLARY FOR AMERICA', 10000),('C00507574', 'HILLARY FOR AMERICA', 10000),('C00413716', 'HILLARY FOR AMERICA', 10000)]
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
