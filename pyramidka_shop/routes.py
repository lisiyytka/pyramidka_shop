def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('result', '/result')
    config.add_route('review', '/admin/review')
    config.add_route('offices', '/offices')
