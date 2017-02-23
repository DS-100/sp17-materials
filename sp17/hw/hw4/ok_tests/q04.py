test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute(query_q4).fetchall() == [('SOUTHERLAND FOR CONGRESS', 'MARCO RUBIO FOR PRESIDENT'),('DAN COATS FOR INDIANA', 'DONALD J. TRUMP FOR PRESIDENT, INC.'),('LUKE MESSER FOR CONGRESS', 'MARCO RUBIO FOR PRESIDENT'),('LUKE MESSER FOR CONGRESS', 'JEB 2016, INC.'),('SCOTT RIGELL FOR CONGRESS', 'MARCO RUBIO FOR PRESIDENT'),('DAN COATS FOR INDIANA', 'JEB 2016, INC.'),('TEXANS FOR LAMAR SMITH', 'DONALD J. TRUMP FOR PRESIDENT, INC.'),('MICHAEL BURGESS FOR CONGRESS', 'DONALD J. TRUMP FOR PRESIDENT, INC.'),('MOOLENAAR FOR CONGRESS', 'MARCO RUBIO FOR PRESIDENT'),('MEADOWS FOR CONGRESS', 'DONALD J. TRUMP FOR PRESIDENT, INC.')]
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
