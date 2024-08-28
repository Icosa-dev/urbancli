{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
  ];

  shellHook = ''
    python3 app/main.py
    exit
  '';
}