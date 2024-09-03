import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./globals.css";
import "./index.css";

import MyPodPage from "./pages/aula/inicio.tsx";
import { IpodPage } from "./pages/aula/ipod.tsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <MyPodPage />,
  },
  {
    path: "/my-pod/ipod",
    element: <IpodPage />,
  },
]);
createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
