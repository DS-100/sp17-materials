test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute(query_q5).fetchall() == [('RUBIO, MARCO', 'RUBIO, MARCO')]
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
