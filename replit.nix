{ pkgs }: {
  deps = [
    (pkgs.python3.withPackages (ps: with ps; [
      pandas
      numpy
      scikitlearn
      streamlit
      psycopg2
      notebook
      requests
    ]))
  ];
}