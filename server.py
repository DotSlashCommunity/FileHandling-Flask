from flask import Flask, jsonify, request, send_from_directory
import time
import os
import os.path

app = Flask(__name__)


@app.route("/")
def _serve():
    return send_from_directory(".", "index.html")


@app.route("/write")
def _write():
    args = request.args

    if "e" not in args.keys():
        return jsonify({
                "ok": False,
                "msg": "Missing_Expression"
                })

    if args["e"] in ["", None]:
        return jsonify({
                "ok": False,
                "msg": "Empty_Expression"
                })

    value = str(int(time.time()))
    file_name = "%s.txt" % value
    PATH = './%s' % file_name
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        return jsonify({
                "ok": False,
                "msg": "File_Already_Exists"
                })
    else:
        f = open(file_name, "w")
        f.write(args["e"])
        f.close()
        return jsonify({
                "ok": True,
                "msg": "File Saved"
                })


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
