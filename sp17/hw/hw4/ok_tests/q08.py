test = {
  'name': 'Question 8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute(query_q8).fetchall() == [('C00575795', 'HILLARY FOR AMERICA', 0.229135526370839),('C00577130', 'BERNIE 2016', 0.678298121635971)]
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
