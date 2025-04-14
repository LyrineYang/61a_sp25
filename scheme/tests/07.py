test = {
  'name': 'Problem 7',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (lambda (x y) (+ x y)) ;; An lambda procedure is displayed exactly as it is written
          d67e9003bbdbf8509fca26654472810c
          # locked
          scm> (lambda (x)) ; type SchemeError if you think this causes an error
          487e5d855a4749c37e82d995b26091f7
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (lambda (x) (+ x) (+ x x))
          (lambda (x) (+ x) (+ x x))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (lambda () 2)
          (lambda () 2)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> lambda_line = read_line("(lambda (a b c) (+ a b c))")
          >>> lambda_proc = do_lambda_form(lambda_line.rest, env)
          >>> lambda_proc.formals # use single quotes ' around strings in your answer
          7476c3e5acb9272c1fa874fb4706b503
          # locked
          # choice: Pair('a', Pair('b', Pair('c', nil)))
          # choice: Pair('+', Pair('a', Pair('b', Pair('c', nil))))
          # choice: Pair(Pair('a', Pair('b', Pair('c', nil))))
          >>> lambda_proc.body # the body is a *Scheme list* of expressions! Make sure your answer is a properly nested Pair.
          63850387e7e0a61d38198ef86d614d00
          # locked
          # choice: Pair(Pair('+', Pair('a', Pair('b', Pair('c', nil)))), nil)
          # choice: Pair('+', Pair('a', Pair('b', Pair('c', nil))))
          # choice: Pair('+', 'a', 'b', 'c')
          # choice: Pair('a', Pair('b', Pair('c')))
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> lambda_line = read_line("(lambda (x y) x)")
          >>> lambda_proc = do_lambda_form(lambda_line.rest, env)
          >>> isinstance(lambda_proc, LambdaProcedure)
          True
          >>> lambda_proc.env is env
          True
          >>> lambda_proc
          LambdaProcedure(Pair('x', Pair('y', nil)), Pair('x', nil), <Global Frame>)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
