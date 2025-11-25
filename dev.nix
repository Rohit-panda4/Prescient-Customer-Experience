let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    buildInputs = [
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