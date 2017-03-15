test = {
  'name': 'Question 20',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> int(crawl_stats['rmse'].mean()*1000) == 68
          True
          >>> int(crawl_stats['rmse'].std()*1000) == 136
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