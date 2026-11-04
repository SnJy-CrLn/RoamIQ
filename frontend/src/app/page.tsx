import SideBar from "./components/SideBar";
import MainArea from "./components/MainArea";

export default function Home() {
  return (
    <div className="flex min-h-screen min-w-screen">
    <SideBar />
    <MainArea />
    </div>
  );
}
