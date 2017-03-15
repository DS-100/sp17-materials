test = {
  'name': 'Question 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> pdf_q, obs_q = compute_q_q_pairs("http://a.hatena.ne.jp/Syako/simple") 
          >>> # Test the first component of the q_q_pairs function - the pdf
          >>> int(np.mean(pdf_q)) == 358
          True
          >>> int(np.std(pdf_q)) == 204
          True
          >>> # Test the observed values
          >>> int(np.mean(obs_q)) == 371
          True
          >>> int(np.std(obs_q)) == 205
          True
          >>> # Test their interaction
          >>> int(np.mean(pdf_q - obs_q)) == -13
          True
          >>> int(np.std(pdf_q - obs_q)) == 30
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