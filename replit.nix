{ pkgs }: {
    deps = [
        pkgs.bashInteractive
		pkgs.ffmpeg
		pkgs.python310
		pkgs.nodejs-17_x
        pkgs.nodePackages.npm
		pkgs.wget

    ];
}
