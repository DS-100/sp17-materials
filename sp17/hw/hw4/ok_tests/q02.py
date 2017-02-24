test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute(query_q2 + ", state ").fetchall() == [('DC', 166),('CA', 64),('VA', 55),('NY', 48),('TX', 46),('FL', 43),('OH', 38),('PA', 35),('MD', 22),('IL', 18),('CO', 17),('MA', 15),('MI', 15),('AL', 14),('IN', 14),('MN', 14),('NJ', 13),('CT', 11),('GA', 11),('NC', 11),('WA', 10),('TN', 9),('AZ', 8),('LA', 8),('MO', 7),('NV', 7),('OR', 6),('WI', 6),('NM', 5),('RI', 5),('SC', 5),('AR', 4),('DE', 4),('KS', 4),('OK', 4),('WV', 4),('IA', 3),('MS', 3),('NH', 3),('VT', 3),('HI', 2),('SD', 2),('ID', 1),('ME', 1),('MT', 1),('NE', 1),('UT', 1)]
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
