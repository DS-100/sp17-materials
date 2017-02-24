test = {
  'name': 'Question 14',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute("SET SEED TO 0.42; select * from bernie_props limit 5").fetchall() == [(129, 0.721877716603883),(195, 0.718153398478205),(251, 0.723865473972939),(106, 0.716918015820211),(120, 0.681684714507472)]
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
