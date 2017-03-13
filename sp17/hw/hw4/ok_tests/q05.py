test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> student_sol = connection.execute(query_q5).fetchall()
          >>> oldsol = (student_sol == [('BUSH, JEB', 'RUBIO, MARCO'), ('RUBIO, MARCO', 'BUSH, JEB')])
          >>> newsol = (len(student_sol) == 8) # correct usage of state field in comm / inter_comm
          >>> oldsol or newsol
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
