import unittest
from server import app

class RunnnOriginalTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_01_index_html(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'RUNNN', response.data)
        self.assertIn(b'Scirra Construct', response.data)

    def test_02_runtime_scripts(self):
        scripts = [
            '/scripts/main.js',
            '/scripts/c3runtime.js',
            '/scripts/objRefTable.js',
            '/scripts/project/javaScriptInEvents.js',
            '/scripts/c3main.js',
            '/scripts/dispatchworker.js',
            '/scripts/jobworker.js',
            '/scripts/modernjscheck.js',
            '/scripts/supportcheck.js',
            '/scripts/offlineclient.js',
            '/scripts/register-sw.js'
        ]
        for s in scripts:
            res = self.client.get(s)
            self.assertEqual(res.status_code, 200, f"Missing script: {s}")

    def test_03_data_and_config(self):
        configs = [
            '/data.json',
            '/constants.json',
            '/appmanifest.json',
            '/offline.json',
            '/sw.js',
            '/style.css'
        ]
        for c in configs:
            res = self.client.get(c)
            self.assertEqual(res.status_code, 200, f"Missing config: {c}")

    def test_04_media_and_images(self):
        media = [
            '/images/shared-0-sheet0.webp',
            '/media/game/stomp.webm',
            '/media/game/chase.webm',
            '/icons/icon-512.png'
        ]
        for m in media:
            res = self.client.get(m)
            self.assertEqual(res.status_code, 200, f"Missing media: {m}")

if __name__ == '__main__':
    unittest.main()
