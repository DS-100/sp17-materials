test = {
  'name': 'Question 1b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> connection.execute(query_q1b).fetchall() == [('C00496075', 'RAND PAUL FOR PRESIDENT, INC.', 1400000),('C00492785', 'CRUZ FOR PRESIDENT', 250012),('C00027466', 'MARCO RUBIO FOR US SENATE', 46800),('C00252551', 'RAND PAUL FOR PRESIDENT, INC.', 22507),('C00570739', 'CRUZ FOR PRESIDENT', 16978),('C00197863', 'HILLARY VICTORY FUND', 15000),('C00162339', 'ENTERPRISE RENT-A-CAR', 10000),('C00202861', 'TRUMP VICTORY', 10000),('C00374058', 'WINNING CONNECTIONS', 8384),('C00406256', 'HILLARY FOR AMERICA', 5854),('C00570739', 'CRUZ FOR PRESIDENT', 5031)]
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
