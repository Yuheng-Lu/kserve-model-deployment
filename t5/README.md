## Deploy Model

1. Create a namespace to use for deploying KServe resources:

   ```bash
   kubectl create namespace kserve-test
   ```

2. Create an `InferenceService`:

   ```bash
   kubectl apply -f t5.yaml -n kserve-test
   ```

   Wait until `READY` is `True`. Check the status with `kubectl get inferenceservices -n kserve-test`.

3. Start the minikube tunnel (if using minikube):

   ```bash
   minikube tunnel
   ```

## Deploy Streamlit App

1. Build the docker image:

   ```bash
   docker build -t streamlit-t5-app .
   ```

2. Push the Image to a Container Registry:

   ```bash
   docker tag streamlit-t5-app <your-registry>/streamlit-t5-app
   docker push <your-registry>/streamlit-t5-app
   ```

3. Deploy everything with command (replace the registry name in the `t5-app.yaml` file before running the command):

   ```bash
   kubectl apply -f t5-app.yaml
   ```

4. Update `/etc/hosts` with the External IP (minikube tunnel):

   ```bash
   echo "127.0.0.1 streamlit-t5.kserve-test.example.com" | sudo tee -a /etc/hosts
   ```

5. Open browser and go to `http://streamlit-t5.kserve-test.example.com`. The app should be available.
