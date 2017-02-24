test = {
  'name': 'Question 1c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> connection.execute(query_q1c).fetchall() == [('C00492785', 'CRUZ FOR PRESIDENT', 250012), ('C00570739', 'CRUZ FOR PRESIDENT', 30619), ('C00193631', 'MARCO RUBIO FOR U.S. SENATE', 17500), ('C00051979', 'KASICH FOR AMERICA', 15000), ('C00197863', 'HILLARY VICTORY FUND', 15000), ('C00283523', 'CRUZ FOR PRESIDENT', 15000), ('C00296657', 'KASICH FOR AMERICA', 12400), ('C00002469', 'HILLARY FOR AMERICA', 10000), ('C00007542', 'HILLARY FOR AMERICA', 10000), ('C00008268', 'HILLARY FOR AMERICA', 10000), ('C00023580', 'HILLARY FOR AMERICA', 10000), ('C00027342', 'HILLARY FOR AMERICA', 10000), ('C00034488', 'HILLARY FOR AMERICA', 10000), ('C00065219', 'HILLARY FOR AMERICA', 10000), ('C00082040', 'MARCO RUBIO FOR US SENATE', 10000), ('C00105981', 'MARCO RUBIO FOR US SENATE', 10000), ('C00121368', 'MARCO RUBIO FOR US SENATE', 10000), ('C00147975', 'HILLARY FOR AMERICA', 10000), ('C00162339', 'ENTERPRISE RENT-A-CAR', 10000), ('C00188193', 'HILLARY FOR AMERICA', 10000)]
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
