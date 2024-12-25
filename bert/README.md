## Deploy Model

1. Create a namespace to use for deploying KServe resources:

   ```bash
   kubectl create namespace kserve-test
   ```

2. Create an `InferenceService`:

   ```bash
   kubectl apply -f bert.yaml -n kserve-test
   ```

   Wait until `READY` is `True`. Check the status with `kubectl get inferenceservices -n kserve-test`.

3. Start the minikube tunnel (if using minikube):

   ```bash
   minikube tunnel
   ```

## Deploy Streamlit App

1. Build the docker image:

   ```bash
   docker build -t streamlit-bert-app .
   ```

2. Push the Image to a Container Registry:

   ```bash
   docker tag streamlit-bert-app <your-registry>/streamlit-bert-app
   docker push <your-registry>/streamlit-bert-app
   ```

3. Deploy everything with command (replace the registry name in the `bert-app.yaml` file before running the command):

   ```bash
   kubectl apply -f bert-app.yaml
   ```

4. Update `/etc/hosts` with the External IP (minikube tunnel):

   ```bash
   echo "127.0.0.1 streamlit-bert.kserve-test.example.com" | sudo tee -a /etc/hosts
   ```

5. Open browser and go to `http://streamlit-bert.kserve-test.example.com`. The app should be available.
