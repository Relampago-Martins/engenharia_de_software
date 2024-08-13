import "./App.css";
import myPodLogo from "./assets/mypod.gif";

function App() {
  return (
    <div className="bg-gray-100 w-svw h-svh flex flex-col">
      <img src={myPodLogo} className="logo" alt="Vite logo" />

      <span className="text-2xl">Welcome to myPod</span>
    </div>
  );
}

export default App;
