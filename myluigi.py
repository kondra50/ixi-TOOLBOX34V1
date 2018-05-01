import luigi



class ixisync(luigi.Task):

    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget("squares.txt")

    def run(self):
        with self.input()[0].open() as fin, self.output().open('w') as fout:
            for line in fin:
                n = int(line.strip())
                out = n * n
                fout.write("{}:{}\n".format(n, out))

if __name__ == '__main__':
    luigi.run()