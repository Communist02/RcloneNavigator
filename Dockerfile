FROM quay.io/pypa/manylinux_2_34_x86_64

ENV PATH="/opt/python/cp313-cp313/bin:$PATH"
RUN /opt/python/cp313-cp313/bin/pip install --upgrade pip && pip install nuitka

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN cd /opt/_internal && tar xf static-libs-for-embedding-only.tar.xz

COPY app /app/app
COPY translations /app/translations
COPY main.py /app

RUN nuitka --standalone --enable-plugin=pyside6 --product-name="Rclone Navigator" --product-version=1 --output-file=rclone_navigator --include-data-dir=app/resources=app/resources --include-data-dir=translations=translations main.py
