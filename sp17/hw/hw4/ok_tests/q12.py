test = {
  'name': 'Question 12',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute("SET SEED TO 0.42; select * from hillary_trials limit 5").fetchall() == [(129, 59392, 293073),(195, 62719, 244237),(251, 56432, 269367),(106, 59478, 302770),(120, 60159, 291818)]
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
