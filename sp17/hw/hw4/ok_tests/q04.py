test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute(query_q4).fetchall() == [('RAND PAUL FOR US SENATE ', 'RAND PAUL FOR PRESIDENT, INC.')]
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
