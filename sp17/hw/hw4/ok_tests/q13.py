test = {
  'name': 'Question 13',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute("SET SEED TO 0.42; select * from hillary_props limit 5").fetchall() == [(129, 0.202652581438754),(195, 0.256795653402228),(251, 0.209498565154603),(106, 0.19644614724048),(120, 0.206152464892501)]
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
