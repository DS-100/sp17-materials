test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute(query_q2 + ", state ").fetchall() == [('NY', 7),('VA', 7),('OH', 3),('PA', 3),('CO', 2),('DC', 2),('FL', 2),('NH', 2),('NM', 2),('TX', 2),('VT', 2),('GA', 1),('KY', 1),('NJ', 1),('UT', 1),('WV', 1)]
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
