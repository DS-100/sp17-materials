test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(expand_image_range(test_im), [37, 65, 89])
          True
          >>> np.allclose(expand_image_range(test_im + 5), [162, 187, 214])
          True
          >>> np.allclose(expanded1[100][100], [187, 187, 214])
          True
          >>> np.allclose(expanded1[200][200], [214, 214, 240])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> test_im = np.array([
      ...   [ [1, 2, 3] ]
      ... ])
      >>> res_im = np.array([
      ...   [ [37, 65, 89] ]
      ... ])
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
