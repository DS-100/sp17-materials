test = {
  'name': 'Question 1e',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute(query_q1e).fetchall() == [('RAND PAUL FOR US SENATE ', 'RAND PAUL FOR PRESIDENT, INC.', 1400000),('CRUZ FOR PRESIDENT', 'DONALD J. TRUMP FOR PRESIDENT, INC.', 2000)]
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
