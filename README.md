https://examen-final-0tdx.onrender.com/

<br>#Nah me lo mama  visual, voy a hacer con ptcharm, voy a ir añadiendo lo de los modelos a ver
<br> Si te salen mis cambios de los modelos?
<br> SI bro, solo que esque ya le tenia artas cosas, perame yo subo mis cambios y ya me ayudas a seguir con ese a ver que le ves
<br> Dale
<br> bro voy a ir haciendo el coso de los requeriments, mientras subes los cambios, porque me da cosa subir los mios que se choquen con los tuyos
<br>Listo bro, ahí le traté de hacer las relations pero quedé trululu para lo de estadisticas
<br>Si quieres metele tus cambios y miramos a ver que
<br> jsjsjsjss dale, voy a ver que puedo hacer
<br> por cierto hay ya hice lo de los requerimeitnos
<br> si vi, ya le instalé los requirements, si quieres ve haciendo o mirando lo de los models y yo voy haciendo el main
<br> Dale, pos toca instalarle mas requerimiento ajsjasjas. y mirando, sera que dejamos lo de faltas en jugador o en estadisticas?
<br> Dejemosla en estadísticas bro, ahí en las estadisticas jugasdor dice que es importante llevar las faltas y esa joa
<br> Okey dale, mientras voy a ir haciendo los routers de verga
<br> Broooo, yo ya estaba haciendolos JSJJSJSJ
<br> aksjasjas, bro que bueno que lei porque ya les iba a hacer push ajskasjas
<br> bro toca meter los routers en carpetas, no se pueden dejar ahi tirados a la loca
<br>Bro soy una hueva, me comí los cambios que le hiciste a los models, que cambios le has hecho?? para saber en que continuo
<br> JAKSJASAJAS, tranqui, pos lo que hice fue cambiarle de que fuera de int a date en el coso de la fehca de nacimiento, y le añadi el coso de dorsal a jugador 
<br>
<br>  Avamce en la mamada esa de router del jugador pero hay cosas que me las marca como error, no se si en tu visual salga asi?
<br>ya reviso bro, estaba viendo como hacia lo del model de partido pero no se como le podríamos hacer para lo del resultado
<br> esa si no tengo idea
<br>Bro, de donde te guiaste para hacer el router de Jugador, del tuyo si?
<br> si bro, del de cliente de mi proyecto
<br>Listo bro, creo que ya está redi el problema que te daba en jugador
<br> Pos acabe de copiar tu router y aun me aparece subrayado como si hubiera error
<br>SI? dios a mi me aparece que todo anda god, le estoy haciendo es el jugador.html y la navbar para que por lo menos la pagina se vea medio bien, tambien si quieres voy a ver para hacer la principal, osea el index
<br>Dale, pos desde que te ande a ti todo bien, nice, y mirando creo que si va a ser necesario el id, porque hay cosas que por lo visto son necesarias
<br>Y si, voy a crear el fokin id para poder editar y toda la mamamda
<br>Epa si quieres ve mirando eso entonces del id y yo sigo aca con el index que ya voy adelantando 
<br> Brooooo, necesito que vuelvas a desplegar el server (revivan el server) JSJSJS
<br> Ya, pero genero error el hijo de su perra bomba madre


<br>                       ~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/opt/render/project/python/Python-3.13.4/lib/python3.13/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/opt/render/project/src/main.py", line 4, in <module>
    from db import create_db_and_tables
  File "/opt/render/project/src/db.py", line 18, in <module>
    engine = create_engine(DATABASE_URL, echo=False)
  File "<string>", line 2, in create_engine
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 281, in warned
    return fn(*args, **kwargs)  # type: ignore[no-any-return]
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/create.py", line 617, in create_engine
    dbapi = dbapi_meth(**dbapi_args)
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/dialects/postgresql/psycopg2.py", line 696, in import_dbapi
    import psycopg2
ModuleNotFoundError: No module named 'psycopg2'
==> Exited with status 1
==> Common ways to troubleshoot your deploy: https://render.com/docs/troubleshooting-deploys
==> Running 'uvicorn main:app --host 0.0.0.0 --port $PORT'
Traceback (most recent call last):
  File "/opt/render/project/src/.venv/bin/uvicorn", line 8, in <module>
    sys.exit(main())
             ~~~~^^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/click/core.py", line 1485, in __call__
    return self.main(*args, **kwargs)
           ~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/click/core.py", line 1406, in main
    rv = self.invoke(ctx)
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/click/core.py", line 1269, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/click/core.py", line 824, in invoke
    return callback(*args, **kwargs)
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/main.py", line 423, in main
    run(
    ~~~^
        app,
        ^^^^
    ...<46 lines>...
        h11_max_incomplete_event_size=h11_max_incomplete_event_size,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/main.py", line 593, in run
    server.run()
    ~~~~~~~~~~^^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/server.py", line 67, in run
    return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
  File "/opt/render/project/python/Python-3.13.4/lib/python3.13/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "/opt/render/project/python/Python-3.13.4/lib/python3.13/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/opt/render/project/python/Python-3.13.4/lib/python3.13/asyncio/base_events.py", line 725, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/server.py", line 71, in serve
    await self._serve(sockets)
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/server.py", line 78, in _serve
    config.load()
    ~~~~~~~~~~~^^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/config.py", line 439, in load
    self.loaded_app = import_from_string(self.app)
                      ~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/opt/render/project/python/Python-3.13.4/lib/python3.13/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/opt/render/project/src/main.py", line 4, in <module>
    from db import create_db_and_tables
  File "/opt/render/project/src/db.py", line 18, in <module>
    engine = create_engine(DATABASE_URL, echo=False)
  File "<string>", line 2, in create_engine
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 281, in warned
    return fn(*args, **kwargs)  # type: ignore[no-any-return]
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/create.py", line 617, in create_engine
    dbapi = dbapi_meth(**dbapi_args)
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/dialects/postgresql/psycopg2.py", line 696, in import_dbapi
    import psycopg2
ModuleNotFoundError: No module named 'psycopg2'

<br> mira
<br>
<br>
<br> Revisa el router de jugador a ver si te genera error
<br> Ya le arregle unos problemas que aparecian en el router, voy a hacer el commit con otros ajustes que le metí
<br> Bro, vuelve a desplegar el server, a ver si ya llama bien que vi un problema con el router a ver si ya por lo menos nos muestra la pag principal

<br> Eso no carga, lleva 5 mins ahi cargando

<br> esa cosa me genero el mismo error que te apase
